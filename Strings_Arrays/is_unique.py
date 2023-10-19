data = "abc"
# data = "hello"

def is_unique(data):
  return len(set(data)) == len(list(data))

def main():
  print(is_unique(data))

if __name__ == '__main__':
  main()