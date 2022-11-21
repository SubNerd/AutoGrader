import cv2
  
# Function to extract frames
def FrameCapture(path):
      
    # Path to video file
    vidObj = cv2.VideoCapture(path)
  
    # Used as counter variable
    count = 0
  
    # checks whether frames were extracted
    success = 1
  
    while success:
  
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        try:
            # Saves the frames with frame-count
            cv2.imwrite("./lights/frame%d.jpg" % count, image)
    
            count += 1
        except:
            print()
  
# Driver Code
if __name__ == '__main__':
    FrameCapture("final.mp4")