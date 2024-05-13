# HW1

JUN-TEST의 prod, dev 브랜치에는 아직 완성되지 않은 계산기 코드가 있다. 현재는 원하는 메뉴를 고르고 두 숫자를 인풋으로 넣어주면 더하거나 빼주는 기능밖에 존재하지 않는다.

여기에 곱하기와 나누기 기능을 추가하려고 한다.

아래의 조건을 잘 지키면서 기능을 추가해보도록 하자.

## 조건

- prod와 dev 브랜치에는 원격에 직접 푸시하지 않는다. 풀 리퀘스트를 활용하자
  -- 풀 리퀘스트를 올릴 때는 Hyunjun Gil을 reviewer로 지정하도록한다.
- feature 브랜치를 적극적으로 활용하여 실제로 feature를 추가하고 prod에 올리기 까지의 과정을 재현해보도록 하자.
  -- 곱하기와 나누기 기능을 각각 feature1, feature2로 분리해서 추가하도록할 것

# HW2

JUN-TEST의 prod2, dev2 브랜치에는 덧셈, 뺄셈밖에 구현되지 않은 계산기 코드가 있었다. 의욕이 넘쳤던 당신은 팀원과 상의없이 미리 곱셈과 나눗셈 그리고 엄청난 노력을 들여 다양한 함수들을 구현하였고 prod2에 합치려고 했으나 아래와 같은 문제가 발생하였다.

- 곱셈과 나눗셈을 구현하는 과정에서 sub의 코드를 복사하여 붙여넣었는데 수정하지 않는 실수를 저질러 버렸다.
- 팀원과의 상의없이 아래의 3개 커밋을 연달아 원격에 올려버렸다.
  1. 매우 중요한 함수 very_very_important_complex_function을 한 달 동안 밤샘 작업을 통해 구현하여 commit
  2. 그 이후 너무 피곤한 나머지 치명적인 버그를 가진 very_very_fatal_function을 작업하여 commit
  3. 그 위에 복사-붙여넣기가 불가능한 엄청나게 긴 코드인 very_very_noisy_annoying_heavy_function을 구현하여 commit
- 당신이 다양한 함수들을 구현하느라 씨름하는동안 팀원들은 이미 곱셈과 나눗셈, 그리고 몫과 나머지 연산까지 구현하여 prod2에 올려버린 상황이다!

이제 당신은 꼬여버린 dev2 브랜치를 살려내고 당신이 구현한 혁명적인 함수인very_very_important_complex_function과 very_very_noisy_annoying_heavy_function을 prod2 브랜치에 합쳐야 한다. 아래의 조건을 만족하면서 이를 완수해보도록 하자.

## 조건

- 최종 prod2 브랜치에는
  - 곱셈, 나눗셈, 몫, 나머지 함수가 맞게 구현되어 있어야 한다.
  - very_very_noisy_annoying_heavy_function 함수가 없어야한다.
  - very_very_important_complex_function, very_very_noisy_annoying_heavy_function함수가 있어야 한다.
- very_very_important_complex_function, very_very_noisy_annoying_heavy_function함수는 복사 붙여넣기 불가능하고, 다시 구현하는 것도 불가능하다고 가정한다.
  - 여기서는 함수 하나로 표현했지만, 실제로는 당신이 구현한 코드가 여러 개의 커밋에 걸쳐 여러 파일을 수정한 상황일수도 있다. 이럴 경우 단순히 복사-붙여넣기로 해결하는 것은 힘들다.
  - 새로운 브랜치 생성, git force push, cherry-pick, rebase등 최대한 다양한 기능들을 사용하여 해결해보도록 하자.
