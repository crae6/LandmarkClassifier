from customtkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import torch
from torchvision import transforms
import os

LABELS = ["Eiffel Tower", "Geisel Library", "Golden Gate Bridge", "Great Wall of China", "Leaning Tower of Pisa",
          "Mount Rushmore", "Niagara Falls", "Parthenon", "Pyramids of Giza", "Space Needle", "Stonehenge", "Sydney Opera House"]

try:
    alexnet = torch.jit.load(os.path.join('../Checkpoints/AlexNet.pt'))
    alexnet.eval()
    resnet10 = torch.jit.load(os.path.join('../Checkpoints/ResNet10.pt'))
    resnet10.eval()
    resnet34 = torch.jit.load(os.path.join('../Checkpoints/ResNet34.pt'))
    resnet34.eval()
except Exception as e:
    messagebox.showerror("Model Loading Error", f"Failed to load the model: {e}")

transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

def preprocess_image(file_path):
    try:
        img = Image.open(file_path).convert('RGB')
    except Exception as e:
        messagebox.showerror("Image Loading Error", f"Failed to load the image: {e}")
        return None
    img_tensor = transform(img)
    img_tensor = img_tensor.unsqueeze(0)
    return img_tensor

def upload_and_classify_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    try:
        img = Image.open(file_path)
        img = img.resize((256, 256))
        img_display = CTkImage(img, size=(256, 256))
        img_label.configure(image=img_display)
        img_label.image = img_display
    except Exception as e:
        messagebox.showerror("Image Processing Error", f"Failed to process the image: {e}")
        return

    processed_img = preprocess_image(file_path)
    if processed_img is None:
        return

    try:
        with torch.no_grad():
            prediction3 = alexnet(processed_img)
            prediction1 = resnet10(processed_img)
            prediction2 = resnet34(processed_img)
            _, predicted3 = prediction3.max(1)
            _, predicted1 = prediction1.max(1)
            _, predicted2 = prediction2.max(1)
            predicted3 = LABELS[predicted3.item()]
            predicted1 = LABELS[predicted1.item()]
            predicted2 = LABELS[predicted2.item()]
        result_label3.configure(text=f'AlexNet Prediction: {predicted3}')
        result_label1.configure(text=f'ResNet10 Prediction: {predicted1}')
        result_label2.configure(text=f'ResNet34 Prediction: {predicted2}')
    except Exception as e:
        messagebox.showerror("Prediction Error", f"Failed to make a prediction: {e}")

root = CTk()
root.title('Landmark Classifier')
root.geometry("600x600")

set_appearance_mode("Dark")
set_default_color_theme("blue")

# Prediction Frame (Top)
frame_prediction = CTkFrame(root, corner_radius=10)
frame_prediction.pack(fill="x", side="top", padx=100, pady=10)

result_label1 = CTkLabel(frame_prediction, text='ResNet10 Prediction:')
result_label1.pack(side="top")
result_label2 = CTkLabel(frame_prediction, text='ResNet34 Prediction:')
result_label2.pack(side="top")
result_label3 = CTkLabel(frame_prediction, text='AlexNet Prediction:')
result_label3.pack(side="bottom")
result_label4 = CTkLabel(frame_prediction, text='VGG16 Prediction:')
result_label4.pack(side="bottom")

# Image Frame (Middle)
frame_image = CTkFrame(root, corner_radius=10)
frame_image.pack(expand=True, fill="both", side="top", padx=100, pady=10)

img_label = CTkLabel(frame_image, text="")
img_label.pack(fill="both", expand=True)

# Upload Button Frame (Bottom)
frame_upload = CTkFrame(root, corner_radius=10, fg_color="transparent")
frame_upload.pack(fill="both", side="bottom", padx=100, pady=0)

upload_btn = CTkButton(frame_upload, text='Upload Image', command=upload_and_classify_image)
upload_btn.pack()

root.mainloop()
