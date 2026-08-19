import time
import os

class Word_predict_game:
  def __init__(self, word_list):
    self.word_list = word_list
    self.round = 0
    self.score = 0
    self.isPlay=True

    self.set_round()
    self.update_ui()

  def quit_game(self):
    self.isPlay=False

  def update_ui(self):
    os.system("cls" if os.name=="nt" else "clear")
    if self.chance!=7:
      for num in range(6, self.chance-1, -1):
        self.bg[num] = self.human[num]
    else: pass

    print(f"/----\\")
    print(f"|    |  ")
    print(f"|    {self.bg[0]}  ")
    print(f"|   {self.bg[3]}{self.bg[1]}{self.bg[4]} ")
    print(f"|    {self.bg[2]}  ")
    print(f"|   {self.bg[5]} {self.bg[6]} ")
    print("|")
    print("="*20)
    print(f"score: {self.score}\nchance: {self.chance}\nround: {self.round+1}")
    print("="*20+"\n")

    for word in self.answer:
      print(" ",end="")
      print(word,end="")
    print("\n"+"="*20+"\n")

  def set_round(self):
    if self.round > len(self.word_list)-1:
      self.quit_game()
      return

    self.word=[]
    for string in self.word_list[self.round]:
      self.word.append(string)

    self.answer = []
    for sting in range(len(self.word)):
      self.answer.append("_")

    self.human = ["O","|","|","_","_","/","\\"]
    self.bg = [" "," "," "," "," "," "," "]
    self.chance = 7

    if self.isPlay and self.round!=0:
      self.update_ui()
      self.start_game()
    else:
      pass

  def start_game(self):
    if self.isPlay:
      while self.chance > 0:
        input_word = input()
        if input_word==self.word_list[self.round]:
          self.score+=1
          break
        elif input_word=="quit_game":
          self.quit_game()
          break
        elif input_word=="":
          continue
        elif input_word[0] in self.word_list[self.round] and  input_word[0] not in self.answer:
          self.chance-=0
        else:
          self.chance-=1

        for index in range(len(self.word)):
          if input_word[0]==self.word[index]:
            self.answer[index]=self.word[index]
          else:
            pass

        time.sleep(0.001)
        self.update_ui()

      self.update_ui()
      if self.chance==0:
          print("fall, try again!")
      elif self.isPlay:
          print("Congratulations! You guessed the word.")
      else:
        os.system("cls" if os.name=="nt" else "clear")
        print("="*20)
        print("exit")
        print("="*20)
      time.sleep(5)
      self.round+=1
      self.set_round()
    else:
      pass
