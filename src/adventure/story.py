from adventure.utils import read_events_from_file
import random
from rich.console import Console
from rich.text import Text

console = Console()

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[bold red]You stand still, unsure what to do.[/bold red] The forest swallows you."

def left_path(event):
    return f"[bold green]You walk left.[/bold green] [cyan]{event}[/cyan]"

def right_path(event):
    return f"[bold blue]You walk right.[/bold blue] [cyan]{event}[/cyan]"

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    console.print("[bold magenta]You wake up in a dark forest.[/bold magenta] You can go [yellow]left[/yellow] or [yellow]right[/yellow].")
    while True:
        console.print("[bold white]Which direction do you choose?[/bold white] ([green]left[/green]/[blue]right[/blue]/[red]exit[/red]): ", end="")
        choice = input().strip().lower()
        if choice == 'exit':
            console.print("[bold red]You decide to leave the forest. Goodbye.[/bold red]")
            break
        
        console.print(step(choice, events))
        console.print("\n[bold cyan]Thanks for playing[/bold cyan] [green]Enjoy your next journey![/green]")