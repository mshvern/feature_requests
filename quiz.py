# noinspection PyPackageRequirements
from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb6Mkz8W2OIHXfKJCmDCdl4h4p_vQvEwClRUd-U36P3xETzGi43A5TU4b0560lXmDXVZOy2rAchK97yrLnio181xcLduSYf2ZcTq1ChHx5ERAZdsxwCeHpS5UIIN_l6zP_NzcbMhvQb-kU6Gp5ep-bpvx4csnMmI4YZx5dMTxlbeJtO8Xl6BWYdgGIN8lqCyKuDmtD'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
