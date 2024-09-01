letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>" , "jonathon").replace("<|Date|>" , "jun 27 2024"))