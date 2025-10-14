print('—' * 60)
print(f'    {'cm':>6}    {'mm':>6}    {'m':>6}    {'inch':>6}')
print('—' * 60)

for cm in range(1, 101):
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm * 0.3937
    print(f'    {cm:>6.0f}    {mm:>6.0f}    {m:>6.2f}    {inch:>6.1f}')

print('—' * 60)