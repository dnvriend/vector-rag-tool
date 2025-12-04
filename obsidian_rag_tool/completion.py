"""Completion command for obsidian-rag-tool.

Note: This code was generated with assistance from AI coding tools
and has been reviewed and tested by a human.
"""

import click
from click.shell_completion import BashComplete, FishComplete, ShellComplete, ZshComplete


@click.command(name="completion")
@click.argument("shell", type=click.Choice(["bash", "zsh", "fish"], case_sensitive=False))
def completion_command(shell: str) -> None:
    """Generate shell completion script.

    SHELL: The shell type (bash, zsh, fish)

    Install instructions:

    \b
    # Bash (add to ~/.bashrc):
    eval "$(obsidian-rag-tool completion bash)"

    \b
    # Zsh (add to ~/.zshrc):
    eval "$(obsidian-rag-tool completion zsh)"

    \b
    # Fish (add to ~/.config/fish/completions/obsidian-rag-tool.fish):
    obsidian-rag-tool completion fish > ~/.config/fish/completions/obsidian-rag-tool.fish

    \b
    File-based Installation (Recommended for better performance):

    \b
    # Bash
    obsidian-rag-tool completion bash > ~/.obsidian-rag-tool-complete.bash
    echo 'source ~/.obsidian-rag-tool-complete.bash' >> ~/.bashrc

    \b
    # Zsh
    obsidian-rag-tool completion zsh > ~/.obsidian-rag-tool-complete.zsh
    echo 'source ~/.obsidian-rag-tool-complete.zsh' >> ~/.zshrc

    \b
    # Fish (automatic loading)
    mkdir -p ~/.config/fish/completions
    obsidian-rag-tool completion fish > ~/.config/fish/completions/obsidian-rag-tool.fish

    \b
    Supported Shells:
      - Bash (≥ 4.4)
      - Zsh (any recent version)
      - Fish (≥ 3.0)

    \b
    Note: PowerShell is not currently supported by Click's completion system.
    """
    ctx = click.get_current_context()

    # Get the appropriate completion class
    completion_classes: dict[str, type[ShellComplete]] = {
        "bash": BashComplete,
        "zsh": ZshComplete,
        "fish": FishComplete,
    }

    completion_class = completion_classes.get(shell.lower())
    if completion_class:
        completer = completion_class(
            cli=ctx.find_root().command,
            ctx_args={},
            prog_name="obsidian-rag-tool",
            complete_var="_OBSIDIAN_RAG_TOOL_COMPLETE",
        )
        click.echo(completer.source())
    else:
        raise click.BadParameter(f"Unsupported shell: {shell}")
