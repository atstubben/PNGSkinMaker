from PIL import Image
from collections import Counter

# Load base skin (must be 64x64)
skin = Image.open("chimp.png").convert("RGBA")

# Check if its slim or classic model
r, g, b, a = skin.getpixel((54,20))

if a == 0:
    slim = 1
    width, height = 14, 26
    print("The skin is slim.")
else:
    slim = 0
    width, height = 16, 26
    print("The skin will be treated as classic")

# Load overlay image and resize it to Slim: 14x24, Classic: 16x24
overlay = Image.open("door.png").resize((16-2*slim, 26)).convert("RGBA")

#LEFT UPPER RIGHT LOWER

# Crop Main Picture
left = overlay.crop((0,8,4-slim,20))
right = overlay.crop((12-slim,8,16-2*slim,20))
top = overlay.crop((4-slim,0,12-slim,8))
center = overlay.crop((4-slim,8,12-slim,20))
bottomL = overlay.crop((4-slim,20,8-slim,26))
bottomR = overlay.crop((8-slim,20,12-slim,26))

# Paste Main Picture
skin.paste(left,(44,36))
skin.paste(left,(60-slim,52))
skin.paste(right,(52-slim,36))
skin.paste(right,(52,52))
skin.paste(top,(40,8))
skin.paste(top,(56,8))
skin.paste(center,(20,36))
skin.paste(center,(32,36))
skin.paste(bottomL,(4,36))
skin.paste(bottomR,(12,36))
skin.paste(bottomR,(4,52))
skin.paste(bottomL,(12,52))

# Determine border color
borderColor = overlay.getpixel((3, 2))

# Create seam
seam = Image.new("RGBA", (16, 1),(0,0,0,255))
skin.paste(seam,(0,42))
skin.paste(seam,(0,58))

# Create patches
patchArm = Image.new("RGBA", (4, 12), borderColor)
patchFace = Image.new("RGBA", (8, 8), borderColor)
patchShoulder = Image.new("RGBA", (4, 4), borderColor)
patchSlim = Image.new("RGBA", (4-slim, 4), borderColor)

# Place patches
skin.paste(patchArm,(48,52))
skin.paste(patchArm,(56-slim,52))
skin.paste(patchArm,(16,36))
skin.paste(patchArm,(28,36))
skin.paste(patchArm,(40,36))
skin.paste(patchArm,(48-slim,36))

skin.paste(patchShoulder,(20,32))
skin.paste(patchShoulder,(24,32))

skin.paste(patchShoulder,(44,32))
skin.paste(patchShoulder,(48,32))

skin.paste(patchShoulder,(0,36))
skin.paste(patchShoulder,(0,38))

skin.paste(patchShoulder,(8,52))
skin.paste(patchShoulder,(8,54))

skin.paste(patchSlim,(52,48))
skin.paste(patchSlim,(56-slim,48))

skin.paste(patchFace,(32,8))
skin.paste(patchFace,(48,8))
skin.paste(patchFace,(40,0))

#LEFT UPPER RIGHT LOWER!!!

##### Create smudges

# Head
smudgeChin = overlay.crop((4-slim,7,12-slim,8))
smudgeChin2 = smudgeChin.transpose(Image.Transpose.ROTATE_180)

# Legs
smudgeCrotchL = overlay.crop((7,20,8,26))
smudgeCrotchR = overlay.crop((8,20,9,26))

smudgeCrotchTL = overlay.crop((4-slim,20,8-slim,21))
smudgeCrotchTR = overlay.crop((8-slim,20,12-slim,21))
smudgeCrotchTL2 = smudgeCrotchTL.transpose(Image.Transpose.ROTATE_180)
smudgeCrotchTR2 = smudgeCrotchTR.transpose(Image.Transpose.ROTATE_180)

# Arms
smudgeArmL = overlay.crop((3-slim,8,4-slim,20))
smudgeArmR = overlay.crop((12-slim,8,13-slim,20))

# Torso
smudgeBum = overlay.crop((4-slim,19,12-slim,20))
smudgeBum2 = smudgeBum.transpose(Image.Transpose.ROTATE_180)

# Place smudges
skin.paste(smudgeChin,(48,4))
skin.paste(smudgeChin,(48,5))
skin.paste(smudgeChin,(48,6))
skin.paste(smudgeChin,(48,7))
skin.paste(smudgeChin2,(48,0))
skin.paste(smudgeChin2,(48,1))
skin.paste(smudgeChin2,(48,2))
skin.paste(smudgeChin2,(48,3))

skin.paste(smudgeCrotchL,(11,36))
skin.paste(smudgeCrotchL,(10,36))
skin.paste(smudgeCrotchR,(9,36))
skin.paste(smudgeCrotchR,(8,36))

skin.paste(smudgeCrotchL,(0,52))
skin.paste(smudgeCrotchL,(1,52))
skin.paste(smudgeCrotchR,(2,52))
skin.paste(smudgeCrotchR,(3,52))

skin.paste(smudgeCrotchTL,(4,35))
skin.paste(smudgeCrotchTL,(4,34))
skin.paste(smudgeCrotchTR,(4,33))
skin.paste(smudgeCrotchTR,(4,32))

skin.paste(smudgeCrotchTL2,(4,48))
skin.paste(smudgeCrotchTL2,(4,49))
skin.paste(smudgeCrotchTR2,(4,50))
skin.paste(smudgeCrotchTR2,(4,51))

skin.paste(smudgeBum,(28,35))
skin.paste(smudgeBum,(28,34))
skin.paste(smudgeBum2,(28,33))
skin.paste(smudgeBum2,(28,32))

skin.paste(smudgeArmL,(48-slim,36))
skin.paste(smudgeArmR,(51-slim,36))

skin.paste(smudgeArmL,(48,52))
skin.paste(smudgeArmR,(51,52))

# Save the result
skin.save(f"custom_skin{'_slim' if slim else ''}.png")

#skin.show()