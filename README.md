## Problem Statement:
In a company with limited customer support staff (only 5 agents) and a large number of customers (over 100), managing real-time interactions and minimizing wait times for each customer becomes a significant challenge. Customers need immediate assistance, and any delay in addressing their queries can result in poor customer satisfaction. Additionally, as the customer base grows, it becomes harder to manage support requests efficiently without overwhelming the available agents. The company needs an automated, scalable system to prioritize and handle customer service requests while providing real-time communication between customers and support agents.

## Solution:
The solution to this problem is a real-time support system that integrates a queue management system and a messaging interface for direct communication between customers and agents. By utilizing RabbitMQ for efficient queue management and WebSocket for real-time messaging, the system ensures that all customer requests are managed in an organized manner, with minimal wait times and maximum agent efficiency. The queue system will allow for proper prioritization, while WebSocket communication enables seamless, real-time interaction between customers and support agents.

## Key Features of the Solution:

### Queue Management with RabbitMQ:
- Efficient handling of over 100 customer requests with only 5 agents.
- Prioritization of support tickets based on urgency or customer type.
- Automatic distribution of tasks among available agents.
- Dynamic scaling of support agents to handle varying loads.

### Real-Time Messaging with WebSocket:
- Instant communication between customers and agents, reducing wait time.
- Real-time updates on the customer’s position in the queue.
- Notifications to both customers and agents when an agent is available.

### Agent Dashboard:
- Real-time dashboard to manage customer interactions.
- Visibility into current support requests and customer status.
- Ability to easily switch between active customer chats.

### Timeout Management:
- Time-based rules for customers who take too long to respond.
- Automatic closure of inactive customer sessions to improve system efficiency.

## Technologies Used:
- **Django Rest Framework**: For building the backend API and handling customer interactions.
- **RabbitMQ**: For queue management and ensuring that support tickets are processed in the correct order and handled efficiently by the agents.
- **WebSocket (via Django Channels)**: For establishing real-time communication channels between customers and agents, providing instant feedback and support.
- **Celery**: For managing background tasks like message processing and managing queue consumption from RabbitMQ.
- **Django**: For building the main application structure, including customer support logic, authentication, and communication management.

## Sequence Diagram For The System

![customer support system](https://github.com/user-attachments/assets/995c47bf-28f4-47bd-9b47-616d50655b2a)

## Color Codes 
UI Element	Background	Text Color	Hover Effect
Primary Button	bg-blue-600	text-white	bg-blue-700
Secondary Button	bg-gray-700	text-gray-200	bg-gray-600
Success State	bg-green-600	text-white	bg-green-700
Danger State	bg-red-600	text-white	bg-red-700
Warning State	bg-yellow-500	text-gray-900	bg-yellow-600
Input Fields	bg-gray-700	text-white	focus:ring-blue-500