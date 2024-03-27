import cv2
import os

def get_face_histogram_and_coords(image_path):
    """
    Load an image, detect a face, and return a histogram of the face region along with face coordinates.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if len(faces) == 0:
        return None, None  # No face detected
    
    x, y, w, h = faces[0]
    face_region = gray[y:y+h, x:x+w]
    
    # Calculate histogram of the face region
    hist = cv2.calcHist([face_region], [0], None, [256], [0,256])
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    
    return hist, (x, y, w, h)

def compare_faces(hist1, hist2):
    """
    Compare two face histograms.
    """
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR_ALT)

def main(blacklisted_folder, to_check_folder):
    threshold_value = 0.5 # Example threshold value, modify this based on your testing
    blacklisted_faces = {}
    
    # Load and process each blacklisted image
    for filename in os.listdir(blacklisted_folder):
        hist, _ = get_face_histogram_and_coords(os.path.join(blacklisted_folder, filename))
        if hist is not None:
            blacklisted_faces[filename] = hist
    
    # Check each image in the to_check folder
    for filename in os.listdir(to_check_folder):
        hist, coords = get_face_histogram_and_coords(os.path.join(to_check_folder, filename))
        if hist is not None:
            for _, blacklisted_hist in blacklisted_faces.items():
                similarity = compare_faces(hist, blacklisted_hist)
                if similarity < threshold_value and coords is not None:
                    # Extract filename without extension
                    user_name = os.path.splitext(filename)[0]
                    print(f"{user_name} is blacklisted!")
                    
                    # Display the face region of the blacklisted user
                    image = cv2.imread(os.path.join(to_check_folder, filename))
                    x, y, w, h = coords
                    face_region = image[y:y+h, x:x+w]
                    cv2.imshow(f"{user_name}'s Face", face_region)
                    cv2.waitKey(0)  # Wait for a key press to close the image window
                    cv2.destroyAllWindows()

if __name__ == "__main__":
    main('blacklisted', 'to_check')
