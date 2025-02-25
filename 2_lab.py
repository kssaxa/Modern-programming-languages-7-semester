def parse_input(text):
    if "класс для арифметических операций" in text.lower():
        print(python_arithmetic_class())
        print(cpp_arithmetic_class())
    elif (
        "считает количество слов" in text.lower()
        and "удаляет лишние пробелы" in text.lower()
    ):
        if "Текст:" in text:
            input_string = text.split("Текст:")[1].strip().strip("'")
        else:
            input_string = ""
        print(python_word_count(input_string))
        print(cpp_word_count(input_string))
    elif (
        "принимает список чисел" in text.lower()
        and "удаляет дубликаты" in text.lower()
        and "сортирует" in text.lower()
    ):
        if "Числа:" in text:
            number_list_str = text.split("Числа:")[1].strip().strip("[]")
            numbers = list(map(int, number_list_str.split(",")))
        else:
            numbers = []
        print(python_sort_numbers(numbers))
        print(cpp_sort_numbers(numbers))
    else:
        print("Шаблон не распознан")


def python_arithmetic_class():
    return """
class ArithmeticOperations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b
"""


def cpp_arithmetic_class():
    return """
#include <iostream>

class ArithmeticOperations {
public:
    int add(int a, int b) {
        return a + b;
    }

    int multiply(int a, int b) {
        return a * b;
    }
};
"""


def python_word_count(input_data):
    return f"""
def count_words_and_clean(text):

    cleaned_text = ' '.join(text.split())    
    word_count = len(cleaned_text.split())
    
    return word_count, cleaned_text
    
word_count, cleaned_text = count_words_and_clean({input_data})
        """


def cpp_word_count(input_data):
    return (
        """
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int countWords(text) {
    int wordCount = 0;
    bool inWord = false;

    for (char ch : text) {
        if (!isspace(ch)) {
            if (!inWord) {
                wordCount++;
                inWord = true;
            }
        } else {
            inWord = false;
        }
    }

    return wordCount;
}

string cleanText(const text) {
    string cleanedText;
    bool inWord = false;

    for (char ch : text) {
        if (!isspace(ch)) {
            cleanedText += ch;
            inWord = true;
        } else {
            if (inWord) {
                cleanedText += ' ';
                inWord = false;
            }
        }
    }

    if (!cleanedText.empty() && cleanedText[cleanedText.size() - 1] == ' ') {
        cleanedText.pop_back();
    }

    return cleanedText;
}
int main() {
    string text = """
        + input_data
        + """;

    int wordCount = countWords(text);        
    string cleanedText = cleanText(text);  

}
"""
    )


def python_sort_numbers(numbers):
    return f"""
def remove_duplicates_and_sort(numbers):

    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers

numbers = {numbers}
result = remove_duplicates_and_sort(numbers)
        """


def cpp_sort_numbers(numbers):

    return (
        """
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> removeDuplicatesAndSort(const vector<int>& numbers) {
    set<int> unique_numbers(numbers.begin(), numbers.end());
    vector<int> result(unique_numbers.begin(), unique_numbers.end());
     sort(result.begin(), result.end());

    return result;
}

int main() {
    vector<int> numbers = """
        + str(numbers)
        + """;
    vector<int> result = removeDuplicatesAndSort(numbers);

}
"""
    )


parse_input("Создать класс для арифметических операций: сложение и умножение.")
print("-" * 40)

parse_input(
    "Написать функцию, которая считает количество слов в строке и удаляет лишние пробелы. Текст: 'Goodbye world!'"
)
print("-" * 40)

parse_input(
    "Написать функцию, которая принимает список чисел, удаляет дубликаты, сортирует их и возвращает результат. Числа: [1, 3, 1, 2, 4]"
)
print("-" * 40)
