
import typer


''' #TODO plan
- create `app` versiion to be able to create multiple commnads with same CLI executable
- ...
'''


def main(name: str):
    print(f"Hello {name}") #FIXME test - drop me when start final version


if __name__ == "__main__":
    typer.run(main)

