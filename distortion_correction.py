import numpy as np
import cv2 as cv
import imageio


class ImageWrapper:
	def __init__(self):
		self.frames = []

	def add_frame(self, frame):
		self.frames.append(frame)

	def add_frames(self, frames):
		self.frames += frames

	def clear_frames():
		self.frames.clear()

	def write_gif(self, image_path, fps):
		imageio.mimsave(image_path, self.frames, fps=fps)

	@staticmethod
	def write_image(image_path, image):
		imageio.imwrite(image_path, image)



# The given video and calibration data
video_file = 'res/chessboard.mp4'
K = np.array([[1.50442370e+03, 0, 9.65939753e+02],
			  [0, 1.51417734e+03, 5.66894338e+02],
			  [0, 0, 1]]) # Derived from `calibrate_camera.py`
dist_coeff = np.array([0.10460431, -0.05506334,  0.00271136, -0.00119125, -0.62262696])

# Open a video
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

# Run distortion correction
show_rectify = True
map1, map2 = None, None

iwrapper = ImageWrapper()

while True:
	# Read an image from the video
	valid, img = video.read()
	if not valid:
		break
	frame_orig = np.copy(img)
	frame_rectified = None

	# Rectify geometric distortion (Alternative: `cv.undistort()`)
	info = "Original"
	if show_rectify:
		if map1 is None or map2 is None:
			map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
		img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
		info = "Rectified"
		frame_rectified = np.copy(img)
	cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

	# Show the image and process the key event
	cv.imshow("Geometric Distortion Correction", img)
	key = cv.waitKey(10)
	if key == ord(' '):     # Space: Pause
		key = cv.waitKey()
	if key == 27:           # ESC: Exit
		break
	elif key == ord('\t'):  # Tab: Toggle the mode
		if show_rectify:
			frame_orig = cv.resize(frame_orig, (0, 0), fx=0.7, fy=0.7)
			frame_rectified = cv.resize(frame_rectified, (0, 0), fx=0.7, fy=0.7)
			cv.putText(frame_orig, "Original", (10, 25), cv.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0))
			cv.putText(frame_rectified, "Rectified", (10, 25), cv.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0))
			iwrapper.add_frame(frame_orig)
			iwrapper.add_frame(frame_rectified)
		show_rectify = not show_rectify

iwrapper.write_gif("res/corrected.gif", fps=1)
video.release()
cv.destroyAllWindows()
