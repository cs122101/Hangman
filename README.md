# Hangman
-  파이썬에서 이 파일을 import하시면 됩니다.

-  정답 이외에 단어 입력은 맨 처음 입력된 글자로 간주됩니다.

-  나가기는 quit_game을 정확히 입력해주세요.

-  대소문자 차이도 오답 처리입니다. ex) 정답이 apple이면 답안을 Apple로 해도 오답처리

- 사용 예시
  ```bash
  import Hangman.py
  
  #문제로 나올 단어 리스트
  word_list = ["apple","orange","banana"]
  
  game = Word_predict_game(word_list)
  
  #게임시작
  game.start_game()
