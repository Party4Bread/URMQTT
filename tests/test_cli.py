import subprocess


def test_smometest():
    output = subprocess.check_output(["urmqtt", "--help"])
    assert b"Usage" in output
    assert b"urmqtt" in output

    output = subprocess.check_output(["urmqtt_sub", "--help"])
    assert b"Usage" in output
    assert b"urmqtt_sub" in output

    output = subprocess.check_output(["urmqtt_pub", "--help"])
    assert b"Usage" in output
    assert b"urmqtt_pub" in output
