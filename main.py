import random


MAX_LINES = 6
MAX_BET = 10000
MIN_BET = 1

ROWS = 6
COLS = 3

symbol_count = {
  "A" : 3,
  "B" : 5,
  "C" : 5,
  "D" : 7
}

symbol_value = {
  "A" : 15,
  "B" : 10,
  "C" : 6,
  "D" : 5
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
      
  return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
  all_symbols = []
  for symbols, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbols)
    
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(all_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  return columns


def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")

    print()

def deposit():
  while True:
    amount = input("What would you like to Deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0")
    else:
      print("The Deposit must be a number")

  return amount

def get_amount_of_lines():
  while True:
    lines = input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + ") ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines")
    else:
      print("The amount of lines must be a number")

  return lines

def get_bet():
  while True:
    bet_amount = input("How much would you like to bet? $")
    if bet_amount.isdigit():
      bet_amount = int(bet_amount)
      if MIN_BET <= bet_amount <= MAX_BET:
        break
      else:
        print(f"Bet must be between ${MIN_BET} and ${MAX_BET}")
    else:
      print("The Bet must be a number")

  return bet_amount

def spin(balance):
  lines = get_amount_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You do not have enough money to bet that amount. Your current balance is ${balance}")
    else:
      break
    
  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"You won ${winnings}.")
  print(f"You won on lines: ", *winning_lines)
  return winnings - total_bet


def main():
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}")
    answer = input("Press Enter to Spin. (Press q to quit)")
    if answer == "q":
      break
    balance += spin(balance)
    if balance == 0:
      print("You went broke bro")
      break

  print(f"You left with ${balance}.")

main()
