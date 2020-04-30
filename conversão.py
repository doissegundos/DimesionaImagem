import cv2

imagem = cv2.imread(r"imagem.png")

ldpi = cv2.resize(imagem, (32,32), interpolation = cv2.INTER_AREA)

mdpi = cv2.resize(imagem, (48,48), interpolation = cv2.INTER_AREA)

hdpi = cv2.resize(imagem, (72,72), interpolation = cv2.INTER_AREA)

xdpi = cv2.resize(imagem, (96,96), interpolation = cv2.INTER_AREA)

xxdpi = cv2.resize(imagem, (144,144), interpolation = cv2.INTER_AREA)

xxxdpi = cv2.resize(imagem, (192,192), interpolation = cv2.INTER_AREA)


cv2.imwrite(r"caminho",ldpi)
cv2.imwrite(r"mdpi.png",mdpi)
cv2.imwrite(r"hdpi.png",hdpi)
cv2.imwrite(r"xdpi.png",xdpi)
cv2.imwrite(r"xxdpi.png",xxdpi)
cv2.imwrite(r"xxxdpi.png",xxxdpi)

cv2.waitKey(0)
cv2.destroyAllWindows()