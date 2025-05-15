# Pi-Sync 🏢🔐

Pi-Sync is a thesis project designed to revolutionize access control in condominiums by integrating modern technologies with centralized management. The system features a Django Rest Framework API as the central brain, syncing mobile and desktop platforms with Raspberry Pi devices for seamless door management and access tracking.

## Features ✨

### Centralized Dashboard 🖥️

- Built with **C# WinForms**, running on the desktop for admin users.
- Manage users and rooms with full CRUD functionality.
- Log all door access activities for monitoring and security.

### Tenant Mobile App 📱

- **Mobile App**: Developed with Kotlin and Jetpack Compose Material 3 for Android tenants.
- Provides tenants with door access controls and status.

### Access Methods 🔑

1. **Physical Key**: Used only as a backup when the system is not functioning, acknowledging that no system is perfect.
2. **Fingerprint Recognition**: Authenticate users with stored biometric data.
3. **Mobile Control**: Unlock doors via the mobile app over the network.

### Synchronization 🔄

- Real-time syncing of access data and logs between the mobile app, desktop admin dashboard, and Raspberry Pi devices.

## Activity Logging 📝

- Tracks and records door access events, providing a complete audit trail.

## System Architecture 🏗️

- The **Django Rest Framework API** serves as the **central brain** 🧠, managing data, authentication, and synchronization across platforms.
- The **Raspberry Pi 5** acts as a hardware controller 🖲️, directly managing door components like solenoids and fingerprint sensors.

## Repository Structure 📂

```
pi-sync/
├── api/          # Django Rest Framework backend API
                    source code (central brain)
├── android/      # Kotlin-based Android app
                    source code (tenant mobile app)
├── desktop/      # Desktop admin dashboard
                    source code (C# WinForms)
├── postman/      # Postman collection files
                    and endpoints.md for API testing
├── raspberrypi/  # Raspberry Pi source code managing
                    hardware (solenoid, fingerprint, etc.)
```

## Tech Stack 🛠️

### Hardware 💻

- **Raspberry Pi 5**: Hardware controller managing physical door components.

### Software 💾

- **Django Rest Framework**: Backend API serving as the system’s central brain.
- **Kotlin Jetpack Compose**: Mobile app for tenant users.
- **C# WinForms**: Desktop admin dashboard for managing users and logs.
- **Fingerprint Modules**: Integrated with the Raspberry Pi for biometric authentication.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

## About 💡

Pi-Sync is developed as part of our thesis project by Ralph Maron Eda, Jack Cabigayan, Triesha Mae Olunan, and Jezlyn Cabbab. The system aims to enhance security and convenience in condominium access management through synchronized mobile and desktop applications integrated with hardware controllers.
