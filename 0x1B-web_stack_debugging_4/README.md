# Web Stack Debugging #4

## Project Overview

This project focuses on improving the performance and reliability of a web stack by addressing specific issues related to Nginx and system resource limits. The tasks in this project include increasing the file descriptor limit for the Nginx server and adjusting user limits for better performance.

## Tasks

### Task 0: Increase Nginx File Descriptor Limit

In this task, we increase the number of file descriptors that the Nginx server can handle by adjusting the `ULIMIT` value in the `/etc/default/nginx` file. This change is necessary to handle a higher amount of traffic on the server.

- **Implementation**: 
  - Modify the `ULIMIT` value from `15` to `4096` in the `/etc/default/nginx` file.
  - Restart the Nginx service to apply the changes.

### Task 1: Adjust User Limits for the Holberton User

In this task, we increase the hard and soft file limits for the `holberton` user in the `/etc/security/limits.conf` file. This adjustment allows the user to open a larger number of files without encountering errors.

- **Implementation**: 
  - Modify the hard file limit for `holberton` to `50000`.
  - Modify the soft file limit for `holberton` to `50000`.

## Usage

To apply the changes, use the provided Puppet scripts. The scripts will automatically modify the necessary configuration files and restart the required services.

1. **Task 0**: 
    - Run the script to increase the Nginx file descriptor limit and restart the service.
  
2. **Task 1**:
    - Run the script to increase the file limits for the `holberton` user.

## Notes

- Ensure that you have the necessary permissions to modify system configuration files.
- Changes to `/etc/security/limits.conf` may require the user to log out and back in for the new limits to take effect.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Your Name** - Initial work - [Your GitHub Username](https://github.com/yourusername)

