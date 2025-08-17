# 🧙 Invisible Cloak using OpenCV

This project implements the famous **Harry Potter–style Invisible Cloak effect** using **Python + OpenCV**.  
By detecting a specific cloak color (default: red) and replacing it with the background, the wearer appears invisible in real-time video.

---

## ✨ Features
- Real-time video processing using OpenCV  
- Cloak detection using HSV color space  
- Image masking & segmentation  
- Beginner-friendly implementation  

---

## 🛠 Tech Stack
- **Python**  
- **OpenCV**  
- **NumPy**  

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/invisible-cloak.git
   cd invisible-cloak

2. **Install dependencies**
   ```bash
   pip install opencv-python numpy

3. **Run the project**
   ```bash
   python.py

  ▶️ Usage

Run the script — your webcam will open.

Wait 2–3 seconds while the camera captures the background.

Hold a red cloak/cloth in front of you → it becomes invisible!

Press q to exit the program.

🎨 Customization

To use a different cloak color, adjust the HSV range in the code:

lower_color = np.array([H_min, S_min, V_min])
upper_color = np.array([H_max, S_max, V_max])


Example: change from red to blue/green/yellow.

📸 Demo

Here’s the Invisible Cloak in action:

![Cloak Demo](assets/81104harry-potter-cloak.jpg)
![cloak Demo](assets/images.jpeg)

📚 Skills Learned

Real-time video capture & processing

Color segmentation in HSV space

Image masking & blending techniques

Problem-solving & debugging in OpenCV

💡 Takeaway

This project shows how code + creativity + computer vision can create fun experiences, not just solve problems.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.






