import cv2
import numpy as np

def canny_edge_detector(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # before canny function converting image to gray scale is required, but if you do not do it, canny function in CV2 do it by itself.
    
    blur = cv2.GaussianBlur(image, (5,5), 0)
    edges = cv2.Canny(blur, 50, 150)
    
    # edges = cv2.Canny(image, 50, 150)
    return edges

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    #  polygon = np.array([[
    #     (0, height),
    #     (width, height),
    #     (width, int(height * 0.6)),
    #     (0, int(height * 0.6))
    # ]], np.int32)
    # cv2.fillPoly(mask, polygon, 255)
    
    rows, cols = edges.shape[:2]
    bottom_left  = [cols * 0.1, rows * 0.95]
    top_left     = [cols * 0.4, rows * 0.6]
    bottom_right = [cols * 0.9, rows * 0.95]
    top_right    = [cols * 0.6, rows * 0.6]
    vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, 255)
    
    masked_image = cv2.bitwise_and(edges, mask)
    return masked_image

def hough_transform(edges):
    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=5
    )
    return lines

def draw_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
    combined_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    return combined_image

def process_frame(frame):
    edges = canny_edge_detector(frame)
    cropped_edges = region_of_interest(edges)
    lines = hough_transform(cropped_edges)
    lane_image = draw_lines(frame, lines)
    return lane_image

# video is read here.
videoFrames = cv2.VideoCapture('road.mp4')
while(videoFrames.isOpened()):
    success, frame = videoFrames.read()
    if not success:
        break
    lane_frame = process_frame(frame)
    cv2.imshow("Lane Detection", lane_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
videoFrames.release()
cv2.destroyAllWindows()