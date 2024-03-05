from jinja2 import Template

nginx_conf_template = Template("""
server {
      listen 80;
      server_name {{ sub_domain }}.abiserve.ir;
    
      location / {
            proxy_pass http://127.0.0.1:{{ port }};
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      }
}
""")