from io import StringIO
from release_notes.models import ReleaseNote


def generate_markdown(releaseNote: ReleaseNote) -> StringIO:
    writer = StringIO()

    # writer.write(f"# Release {releaseNote.semanticVersion}\n\n")
    # writer.write("## Release Features\n\n")
    # writer.write(f"{releaseNote.summary}\n\n")
    writer.write("## Changelog\n\n")

    for key, product in releaseNote.changelogs.items():
        writer.write(f"### {key}\n\n")

        if product.changelog.added:
            writer.write("#### Added\n\n")
            for item in product.changelog.added:
                writer.write(f"- {item}\n\n")

        if product.changelog.deleted:
            writer.write("#### Deleted\n\n")
            for item in product.changelog.deleted:
                writer.write(f"- {item}\n\n")

        if product.changelog.fixed:
            writer.write("#### Fixed\n\n")
            for item in product.changelog.fixed:
                writer.write(f"- {item}\n\n")

        if product.changelog.updated:
            writer.write("#### Updated\n\n")
            for item in product.changelog.updated:
                writer.write(f"- {item}\n\n")

    return writer
