#���� ����1
#https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3

#���� ���� ����Ʈ ���� �߰�
def gloryAddList(list,now,k):
    list.append(now)
    list.sort()
    list=list[-k:]  #k���� ��ŭ ������
    return list

#main solution
def solution(k, score):
    glory = []
    answer = []
    #���� ��ǥ
    for now in score:
        glory = gloryAddList(glory,now,k)
        answer.append(min(glory))  #��ǥ���� ����Ʈ �ֽ�ȭ
    return answer