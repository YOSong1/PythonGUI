
'''
[문제]

다음 문자열에 포함된 모든 문자들이 몇 번 사용이 되었는지 셀 수 있는 프로그램을 작성하고자 합니다.
알파벳은 대문자와 소문자가 같은 문자로 생각하고 각각의 사용된 개수를 카운트 하여 출력예와 같은
형식으로 각 문자와 사용 빈도수를 출력하시오.

<요구사항>
- 알파벳은 대문자 또는 소문자가 같은것으로 간주하고 카운트 한다.
  즉, A와 a는 같은 문자로 생각한다.
- 기타 특수 문자도 몇 번 사용이 되었는지 카운트하여 결과를 출력한다.  

<실행결과>

  : 29
, : 4
- : 1
. : 2
a : 24
b : 2
c : 7
d : 11
e : 19
f : 2
g : 8
h : 3
i : 15
j : 1
l : 8
m : 15
n : 17
o : 11
p : 11
r : 17
s : 11
t : 16
u : 7
v : 2
y : 7


'''


s1 = "Python features a dynamic type system and automatic"
s1+="memory management and supports multiple programming "
s1+="paradigms, including object-oriented, imperative, functional "
s1+="programming, and procedural styles. "
s1+="It has a large and comprehensive standard library." 


dic = {}

#------------------------------------------------
# 이 부분에 코딩하시오.













#---------여기까지--------------------------------------

for key, val in dic.items():
    print("%s : %d" % (key, val)) 

