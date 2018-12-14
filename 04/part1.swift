import Foundation

func read(_ filename: String) -> [String] {
  let path = "./input.txt"
  guard let text = try? NSString(contentsOfFile: path,
                                 encoding: String.Encoding.utf8.rawValue) as String else {
    print("File could not be opened")
    return []
  }

  return text.components(separatedBy: "\n")
}

struct Guard {
  
}

let lines = read("input.txt").sorted()

print(lines.count)
