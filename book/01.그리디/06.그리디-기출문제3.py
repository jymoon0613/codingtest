# 문자열 뒤집기

S = input()

cnt0 = 0
cnt1 = 0

if S[0] == '0':
    cnt0 += 1
    
else:
    cnt1 += 1
    
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            cnt0 += 1
            
        else:
            cnt1 += 1

res = min(cnt0, cnt1)