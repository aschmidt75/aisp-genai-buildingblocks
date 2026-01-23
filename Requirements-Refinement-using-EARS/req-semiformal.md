# EARS-Derived Requirements

## Source Requirement

**R1 (Original):**
> The system shall have a login mechanism using authentication styles like OAuth2, OIDC, that allows for Multi-Factor Authentication (MFA) and allow for basic Conditional Access mechanisms such as blocking IPs (e.g. per country) and time-based restriction (e.g. blocking access outside of office hours)

---

## Analysis

The original requirement R1 violates EARS principles by combining multiple concerns into a single statement. According to the EARS formalization, requirements should be atomic and follow specific patterns.

### Issues Identified

| Issue | Description |
|-------|-------------|
| Multiple concerns | Combines 6+ distinct capabilities in one requirement |
| Vague language | "like OAuth2, OIDC", "basic", "such as" are imprecise |
| Missing testability | No clear acceptance criteria for each capability |
| No temporal ordering | Mixes always-active with conditional behaviours |

---

## Derived EARS Requirements

### Authentication Core

#### R1.1 - Login Mechanism (Ubiquitous)
> **The system shall** provide a login mechanism for user authentication.

- **Pattern:** Ubiquitous
- **Keywords:** THE, SHALL
- **Rationale:** Core capability that is always required

#### R1.2 - OAuth2 Support (Ubiquitous)
> **The system shall** support OAuth2 as an authentication protocol.

- **Pattern:** Ubiquitous
- **Keywords:** THE, SHALL
- **Rationale:** Specified authentication standard

#### R1.3 - OIDC Support (Ubiquitous)
> **The system shall** support OpenID Connect (OIDC) as an authentication protocol.

- **Pattern:** Ubiquitous
- **Keywords:** THE, SHALL
- **Rationale:** Specified authentication standard

---

### Multi-Factor Authentication

#### R1.4 - MFA Capability (Ubiquitous)
> **The system shall** support Multi-Factor Authentication (MFA).

- **Pattern:** Ubiquitous
- **Keywords:** THE, SHALL
- **Rationale:** MFA support is a core capability

#### R1.5 - MFA Enforcement (Optional Feature)
> **Where** MFA is enabled for a user account, **the system shall** require multi-factor authentication during login.

- **Pattern:** Optional Feature (WHERE)
- **Keywords:** WHERE, THE, SHALL
- **Rationale:** MFA enforcement depends on configuration

---

### Conditional Access - IP-Based

#### R1.6 - IP Blocking Configuration (Ubiquitous)
> **The system shall** provide configuration for blocking login attempts based on IP address country of origin.

- **Pattern:** Ubiquitous
- **Keywords:** THE, SHALL
- **Rationale:** Configuration capability is always available

#### R1.7 - IP Blocking Enforcement (Unwanted Behaviour)
> **If** a login attempt originates from a blocked country, **then the system shall** deny the login attempt and log the rejection.

- **Pattern:** Unwanted Behaviour (IF-THEN)
- **Keywords:** IF, THEN, THE, SHALL
- **Rationale:** Response to unauthorized access from blocked region

---

### Conditional Access - Time-Based

#### R1.8 - Time Restriction Configuration (Ubiquitous)
> **The system shall** provide configuration for time-based access restrictions.

- **Pattern:** Ubiquitous
- **Keywords:** THE, SHALL
- **Rationale:** Configuration capability is always available

#### R1.9 - Time Restriction Enforcement (State-Driven)
> **While** the current time is outside the configured access hours, **the system shall** deny login attempts and log the rejection.

- **Pattern:** State-Driven (WHILE)
- **Keywords:** WHILE, THE, SHALL
- **Rationale:** Denial is active during the restricted time state

#### R1.10 - Time Restriction Override (Complex)
> **While** time-based restrictions are active, **when** an administrator grants an exception for a user, **the system shall** permit the login attempt.

- **Pattern:** Complex (WHILE + WHEN)
- **Keywords:** WHILE, WHEN, THE, SHALL
- **Rationale:** Exception handling within time-restricted state

---

## Requirements Summary

| ID | Pattern | Keywords | Description |
|----|---------|----------|-------------|
| R1.1 | Ubiquitous | THE, SHALL | Login mechanism |
| R1.2 | Ubiquitous | THE, SHALL | OAuth2 support |
| R1.3 | Ubiquitous | THE, SHALL | OIDC support |
| R1.4 | Ubiquitous | THE, SHALL | MFA capability |
| R1.5 | Optional Feature | WHERE, THE, SHALL | MFA enforcement |
| R1.6 | Ubiquitous | THE, SHALL | IP blocking config |
| R1.7 | Unwanted Behaviour | IF, THEN, THE, SHALL | IP blocking enforcement |
| R1.8 | Ubiquitous | THE, SHALL | Time restriction config |
| R1.9 | State-Driven | WHILE, THE, SHALL | Time restriction enforcement |
| R1.10 | Complex | WHILE, WHEN, THE, SHALL | Time restriction override |

---

## Traceability Matrix

```
R1 (Original)
├── R1.1  Login mechanism
├── R1.2  OAuth2 support
├── R1.3  OIDC support
├── R1.4  MFA capability
│   └── R1.5  MFA enforcement (conditional)
├── R1.6  IP blocking configuration
│   └── R1.7  IP blocking enforcement
├── R1.8  Time restriction configuration
│   ├── R1.9  Time restriction enforcement
│   └── R1.10 Time restriction override
```
