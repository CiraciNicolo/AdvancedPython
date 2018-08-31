from far import *

if __name__ == "__main__":
    paths = ["w1e8n3w2", "s7n1w3w5e2", "n2w3s1e1",
        "n3w2s1e2", "n3w4e1n4w2e1w5s2n7"]

    for s in paths:
        print("The path \"{}\" corresponds to {:.2f} meters".format(s, far(s)))
