test = "iam testing if this [code] will be returned"


def parse3(test_subject):
    print(test_subject)
    print(test_subject.join(test.split("[" or "]")[3:5]))


parse3(" Maacdonald")
