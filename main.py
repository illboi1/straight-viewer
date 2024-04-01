import imageio
from camera_calibration import select_img_from_video, calib_camera_from_chessboard


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



if __name__ == '__main__':
	video_file = 'res/chessboard.mp4'
	board_pattern = (7, 7)
	board_cellsize = 0.025

	iwrapper = ImageWrapper() # To write gif
	img_select = select_img_from_video(video_file, board_pattern, img_wrapper=iwrapper)
	assert len(img_select) > 0, 'There is no selected images!'
	rms, K, dist_coeff, rvecs, tvecs = calib_camera_from_chessboard(img_select, board_pattern, board_cellsize)

	# Print calibration results
	print('## Camera Calibration Results')
	print(f'* The number of selected images = {len(img_select)}')
	print(f'* RMS error = {rms}')
	print(f'* Camera matrix (K) = \n{K}')
	print(f'* Distortion coefficient (k1, k2, p1, p2, k3, ...) = {dist_coeff.flatten()}')