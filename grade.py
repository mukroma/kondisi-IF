tugas=float(input("masukan nilai tugas"))
pts=float(input("masukan nilai pts"))
pas=float(input("masukan nilai pas"))

nilai=(0.15+tugas)+(0.35+pts)+(0.50+pas)

if nilai > 80:
    grade='A'
elif nilai > 70:
    grade='B'
elif nilai > 60:
    grade='C'
elif nilai > 50:
    grade='D'
else:
    grade="E"

if nilai>60:
    status='lulus'
else:
    status='tidak lulus'

print('nilai akhir : %0.2f' % nilai)
print('grade: {}'.format(grade))
print('status: {}'.format(status))



