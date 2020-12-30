#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from PIL import ImageOps, Image, ImageFont, ImageDraw
from thumbor.filters import BaseFilter, filter_method


class Filter(BaseFilter):
    @filter_method(
        BaseFilter.String,#word
        BaseFilter.String,#type
    )
    def spatial_mark(self, word, type="center", alpha = 90):
        backgroundImage = self.engine.image
        fontSize = 45
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", fontSize)
        width, height = font.getsize(word)
        txtImage=Image.new('RGBA', (width, height), (0, 0, 0, 0))
        drawer = ImageDraw.Draw(txtImage)
        drawer.text((0, 0), word, fill=(0, 0, 0, alpha), font=font)
        if type == 'center':
            rotatedText = txtImage.rotate(angle=45, expand = 1)
            bgHeight, bgWidth = backgroundImage.size
            textHeight,textWidth = rotatedText.size
            x = bgHeight/2 - textHeight/2
            y = bgWidth/2 - textWidth/2
            backgroundImage.paste(im=rotatedText, box=(x, y), mask=rotatedText)
        else:
            backgroundImage.paste(im=txtImage, box=(10, 10), mask=txtImage)
            
        self.engine.image = backgroundImage
