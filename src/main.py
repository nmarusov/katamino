"""Main module"""

from time import time

import click

import solver


@click.command()
@click.option("-l", "--level", default=3, help="Level (field width).")
@click.option(
    "-g",
    "--greedy",
    is_flag=True,
    show_default=True,
    default=False,
    help="Save all solutions for each shape set\
(rotated, flipped, alternative).",
)
@click.argument("filename")
def cli(level, greedy, filename):
    """Katamino solver."""
    print(f"Starting katamino solver for level {level}...")
    solution_set = set()
    count = 0
    tic = time()

    with open(filename, "w", encoding="utf-8") as f:
        for solution in solver.solve(level=level):
            tag = set(solution)
            tag.remove("\n")
            tag = "".join(sorted(tag))

            if greedy:
                if solution in solution_set:
                    continue
                solution_set.add(solution)
            else:
                if tag in solution_set:
                    continue
                solution_set.add(tag)

            count += 1
            message = f"Level: {level}, solution: {count}, tag: {tag}"
            f.write(message + "\n")
            f.write(solution)
            f.write("\n" + "-" * 80 + "\n")  # add a line break
            f.flush()
            print(message)

        toc = time()
        t = f"Elapsed time: {toc - tic:0.3f} s"
        f.write(t)
        print(t)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
