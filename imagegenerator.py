import PIL.Image
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random


class DivisionGenerator():



    def generator(self, div_tier_sq, div_lp_sq, div_rank_sq, winratio_sq, div_tier_flex, div_lp_flex, div_rank_flex, winratio_flex, user_name):
        icon_random = random.randint(0,383)
        bg_random = random.randint(1,10)

        icon = Image.open(f'data1/icons/{icon_random}.png')
        font_soloq = ImageFont.truetype('data1/fonts/Franklin Gothic Medium Regular.ttf', 45) # Font SoloQ
        font_flex = ImageFont.truetype('data1/fonts/Franklin Gothic Medium Regular.ttf', 35) # Font Flex
        font_name = ImageFont.truetype('data1/fonts/nasalization-rg.otf', 90) # Font summoner name

        soloq_div = Image.open(f'data1/soloq div/{div_tier_sq}.png') # SoloQ image div
        flex_div = Image.open(f'data1/flex div/{div_tier_flex}.png') # Flex image div
        bg = Image.open(f'data1/bg/{bg_random}.jpg') # background
        bg.paste(soloq_div, box=(463,193), mask=soloq_div) # soloq div
        bg.paste(flex_div, box=(122,343), mask=flex_div) # flex div
        bg.paste(icon, box=(39,33), mask=icon) # icon

        bg_text = ImageDraw.Draw(bg)
        bg_text.text((654,238), 'SoloQ', font=font_soloq, stroke_width=2, stroke_fill='black', anchor='mm')
        bg_text.text((251,358), 'Flex', font=font_flex, stroke_width=2, stroke_fill='black', anchor='mm')
        bg_text.text((661,576), f"{div_tier_sq} {div_rank_sq} {div_lp_sq} LP", font=font_soloq, stroke_width=2, stroke_fill='black',anchor='mm') # soloq
        bg_text.text((661,635), f"{winratio_flex}% WR", font=font_soloq, stroke_width=2, stroke_fill='black', anchor='mm') # soloq wr
        bg_text.text((255,596), f"{div_tier_flex} {div_rank_flex} {div_lp_flex} LP", font=font_flex, stroke_width=2, stroke_fill='black', anchor='mm') # flex
        bg_text.text((255,632), f'{winratio_sq}% WR', font=font_flex, stroke_width=2, stroke_fill='black', anchor='mm') # flex wr
        bg_text.text((240,63), f'{user_name}', font=font_name, stroke_width=2, stroke_fill='black', anchor='lm') # summoner name





        bg.save('data1/ready.png')
