# CampusConnect Security

## Security Principles

### RSA
RSA provides confidentiality through encryption and supports authentication and non-repudiation using public and private keys.

### Diffie-Hellman
Diffie-Hellman is a key exchange protocol. It securely creates a shared secret but does not encrypt messages.

## Threat Model

### Firewall
A hardware firewall should be placed between the Internet and the CampusConnect server. It should allow only HTTPS (port 443) and block unnecessary traffic.

### IDS
A Network IDS monitors incoming and outgoing traffic, while a Host IDS monitors activity on the server. Using both provides better protection.

### HTTP vs HTTPS
CampusConnect should use HTTPS. HTTPS prevents credential theft, session hijacking, and packet sniffing.

### Authentication
Use multi-factor authentication with:
- Password
- OTP or Authenticator App

Permissions:
- Student: View courses and submit assignments
- Instructor: Manage courses and grades
- Admin: Full system control

### Attack
A Man-in-the-Middle attack is an active attack where an attacker intercepts communication between the user and the server. HTTPS helps prevent this attack.
