import json
import os
import random

DATA_FILE = "words.json"


def load_words():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_words(words):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)


def add_word(words):
    word = input("영어 단어: ").strip()
    if not word:
        print("단어를 입력해주세요.")
        return
    if word in words:
        print(f"'{word}'는 이미 등록된 단어입니다. (뜻: {words[word]})")
        return
    meaning = input("한국어 뜻: ").strip()
    if not meaning:
        print("뜻을 입력해주세요.")
        return
    words[word] = meaning
    save_words(words)
    print(f"✓ '{word}' 추가 완료!")


def list_words(words):
    if not words:
        print("등록된 단어가 없습니다.")
        return
    print(f"\n총 {len(words)}개의 단어:")
    print("-" * 30)
    for word, meaning in sorted(words.items()):
        print(f"  {word:<20} {meaning}")
    print("-" * 30)


def delete_word(words):
    word = input("삭제할 영어 단어: ").strip()
    if word not in words:
        print(f"'{word}'을(를) 찾을 수 없습니다.")
        return
    del words[word]
    save_words(words)
    print(f"✓ '{word}' 삭제 완료!")


def quiz(words):
    if len(words) < 1:
        print("단어가 1개 이상 있어야 퀴즈를 시작할 수 있습니다.")
        return

    items = list(words.items())
    random.shuffle(items)
    score = 0

    print(f"\n퀴즈 시작! (총 {len(items)}문제, 종료하려면 'q' 입력)")
    print("-" * 30)

    for i, (word, meaning) in enumerate(items, 1):
        answer = input(f"[{i}/{len(items)}] '{word}'의 뜻은? ").strip()
        if answer.lower() == "q":
            break
        if answer == meaning:
            print("  정답!")
            score += 1
        else:
            print(f"  오답. 정답: {meaning}")

    print(f"\n결과: {score}/{len(items)} 정답")


def main():
    print("=== 단어장 프로그램 ===")
    words = load_words()

    menu = {
        "1": ("단어 추가", add_word),
        "2": ("단어 목록 보기", list_words),
        "3": ("단어 삭제", delete_word),
        "4": ("퀴즈", quiz),
        "5": ("종료", None),
    }

    while True:
        print("\n메뉴:")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")

        choice = input("선택: ").strip()

        if choice == "5":
            print("종료합니다.")
            break
        elif choice in menu:
            label, func = menu[choice]
            func(words)
        else:
            print("올바른 메뉴를 선택해주세요.")


if __name__ == "__main__":
    main()
