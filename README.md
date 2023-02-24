# Furniture_Classification
A furniture classification product designed based on neural network and deep learning.Alexnet is used as the backbone to extract features and two fully connected layers are connected for classification. The loss function adopts cross entropy loss. Optimizer uses SGD for training.
The product uses the FastAPI framework, which is simple and efficient. At the same time, it cooperates with a CI/CD pipeline that requires a complete set of products. It improves the efficiency of maintenance and improvement
## Installation
1.Clone the repository.  

2.Install the required dependencies with ***pip install -r requirements.txt***.
## Usage
### Local Deploy
1.start the server by running ***python app.py*** in your terminal or command prompt.

2.Open your browser and navigate to http://127.0.0.1:8000/docs#/

3.Interact with the application.
### Running with Docker
To run this application using Docker, follow these steps:

1.Make sure Docker is installed on your machine. If it is not, you can download and install it from the official Docker website: https://www.docker.com/get-started.

2.Build the Docker image for your application by running the following command in the project directory:***docker build -t my_app*** .

3.Once the image is built, you can run a container using the following command:***docker run -p 8000:8000 my_app***.

4.You should now be able to access your application by visiting ***http://localhost:8000/docs#/*** in your web browser.

5.Interact with the application.
## Contact
Yubo Wang- yubowang9609@gmail.com

Project Link: https://github.com/YuboWang96/Furniture_Classification.git
