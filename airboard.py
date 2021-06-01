import calibrator as cal
import detector as det
import tracker
import cv2
from os import system

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = tracker.handDetector(maxHands=1)
locations = cal.calibrate(cap, detector, 26)

# locations = [('q', 545, 341), ('w', 547, 349), ('e', 528, 353), ('r', 503, 347), ('t', 480, 347), ('y', 452, 345), ('u', 425, 344), ('i', 398, 342), ('o', 373, 341), ('p', 348, 340), ('a', 323, 337), ('s', 546, 323), ('d', 514, 320), ('f', 498, 327), ('g', 473, 322), ('h', 447, 324), ('j', 420, 324), ('k', 392, 324), ('l', 369, 321), ('z', 338, 320), ('x', 528, 289), ('c', 503, 302), ('v', 481, 304), ('b', 459, 304), ('n', 424, 305), ('m', 403, 305)]

print('\nKeyboard Coordinates:\n', locations)

n = 0
while True:
	n += 1
	coords = det.scan(cap, detector, n)

	if coords:
		_, x, y = coords[8]

		key, best = det.closest(locations, x, y)

		system('cls')
		print('ITERATION:', n)
		print('\nKey:', key)
		print(f'\nCertainty: {100 - best}%')
