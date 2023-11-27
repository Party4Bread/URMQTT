# 예제에 대한 보충 설명 자료

## 예명 config에 대한 설명

예제 config는 다음과같습니다.
```js
{
    "data-filter":{ // 데이터 전송 차단용 필터
        "enabled": true,
        "plugins": ["lua_filter","py_filter"],
        "filter":[{
            "topic":["temperature/get"], // 적용할 Topic
            "type":"lua", // 함수의 언어.
            "src":"(function(x) return tonumber(x)~=nil end)" // 적용할 filter 함수 
        }]
    },
    "data-map": { // 데이터 변환용 필터
        "enabled": true,
        "plugins": ["lua_map","py_map"], 
        "mapper":[{ // 화씨->섭씨 변환용 필터
            "topic":["temperature/get"],
            "type":"lua",
            "src":"(function(x) return tostring((tonumber(x)-32)*5/9) end)"
        },{ // 4도씩 끊어 전달하는 필터.
            "topic":["temperature/get"],
            "type":"lua",
            "src":"(function(x) return tostring(math.floor((tonumber(x)/4))*4) end)"
        }]
    }
}
```

ACL 
```js
{
    "group":{
        "super":["user:test","user:admin"] //user test와 admin을 super라는 group으로 선언합니다.
    },
    "acls":[
        {"type":"pub/sub","action":"allow",
        "src":["group:super"], //super에게 온도값 topic과 문열기 신호 topic pubsub권한을 부여합니다.
        "dst":["temperature/get","door/unlock"]},
        {"type":"pub/sub","action":"allow",
        "src":["user:temperature"], //temperature에게 온도값 topic의 pubsub권한을 부여합니다.
        "dst":["temperature/get"]},
        {"type":"pub/sub","action":"allow",
        "src":["user:door"],  //door에게 문열기신호 topic의 pubsub권한을 부여합니다.
        "dst":["door/unlock"]}
    ]
}

```

## 동작하는 구조

Publish 패킷을 받았을때 해당 패킷을 deep inspect합니다.
각 JSON에 정의된 필터를 통해 패킷 요청을 drop하거나 data필드를 변환하여 publish queue로 전달합니다.

## 코드 변경점.

lua가 동작합니다