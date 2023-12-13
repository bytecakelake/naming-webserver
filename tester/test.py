from pydantic import BaseModel
import argparse

class cmd(BaseModel):
    host: str


if __name__ == "__main__":
    import sys
    print(sys.argv)
    a = cmd()