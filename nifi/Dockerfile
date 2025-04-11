FROM apache/nifi:latest

# Switch to root to modify file permissions
USER root

# RUN pip install kafka
# # Modify nifi.properties for HTTP access on port 8082
# RUN sed -i \
#   -e 's|^nifi.web.https.host=.*|#nifi.web.https.host=|' \
#   -e 's|^nifi.web.https.port=.*|#nifi.web.https.port=|' \
#   -e '$a\nifi.web.http.host=0.0.0.0' \
#   -e '$a\nifi.web.http.port=8082' \
#   /opt/nifi/nifi-current/conf/nifi.properties

# # Expose HTTP port
# EXPOSE 8082

# # Add custom entrypoint script
# COPY run.sh /opt/nifi/run.sh

# # Change permission of run.sh (now as root)
# RUN chmod +x /opt/nifi/run.sh

# # Switch back to nifi user if necessary
# USER nifi

# # Use the script as entrypoint
# ENTRYPOINT ["/opt/nifi/run.sh"]
