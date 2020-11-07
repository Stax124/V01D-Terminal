import hashlib
import argparse

class c:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

def hashfilesum(target, hashalg) -> None:
    with open(target, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hashalg.update(chunk)

def hash(splitInput) -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("method", help="What method to use", choices=["sha1","sha224","sha256","sha384","sha384","sha512","md5","sha1sum","sha224sum","sha256sum","sha384sum","sha512sum","md5sum"])
    parser.add_argument("target", help="Target to hash", type=str)
    try:
        args = parser.parse_args(splitInput)
    except SystemExit:
        return


    if args.method == "sha1":
        return(hashlib.sha1(bytes(args.target, "utf-8")
                            ).hexdigest())
    elif args.method == "sha224":
        return(hashlib.sha224(bytes(args.target, "utf-8")
                                ).hexdigest())

    elif args.method == "sha256":
        return(hashlib.sha256(bytes(args.target, "utf-8")
                                ).hexdigest())

    elif args.method == "sha384":
        return(hashlib.sha384(bytes(args.target, "utf-8")
                                ).hexdigest())

    elif args.method == "sha512":
        return(hashlib.sha512(bytes(args.target, "utf-8")
                                ).hexdigest())

    elif args.method == "md5":
        return(hashlib.md5(bytes(args.target, "utf-8")
                            ).hexdigest())

    # Hash sum -----------------------------------------------

    elif args.method == "sha1sum":
        hashsum = hashlib.sha1()
        hashfilesum(args.target, hashsum)
        return(hashsum.hexdigest())

    elif args.method == "sha224sum":
        hashsum = hashlib.sha224()
        hashfilesum(args.target, hashsum)
        return(hashsum.hexdigest())

    elif args.method == "sha256sum":
        hashsum = hashlib.sha256()
        hashfilesum(args.target, hashsum)
        return(hashsum.hexdigest())

    elif args.method == "sha384sum":
        hashsum = hashlib.sha384()
        hashfilesum(args.target, hashsum)
        return(hashsum.hexdigest())


    elif args.method == "sha512sum":
        hashsum = hashlib.sha512()
        hashfilesum(args.target, hashsum)
        return(hashsum.hexdigest())

    elif args.method == "md5sum":
        hashsum = hashlib.md5()
        hashfilesum(args.target, hashsum)
        return(hashsum.hexdigest())