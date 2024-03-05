from flask import request
import nginx_utils as nginx
import view_utils as views

def register(app):
      @app.route('/create', methods=['POST'])
      def configure_nginx():
            sub_domain = request.form['sub_domain']
            port = request.form['port']
            return nginx.create_nginx_config(sub_domain, port)

      @app.route('/delete', methods=['POST'])
      def delete_subDomain():
            deleteNameFile = request.form['deleteNameFile']
            return nginx.delete_subDomain_nginx(deleteNameFile)

      @app.route('/show', methods=['POST'])
      def show_subDomains():
            return views.show_all_subDomain()

      @app.route('/search_sub', methods=['POST'])
      def search_sub():
            nameSearch = request.form['nameSearch']
            return views.search_name_subDomain(nameSearch)

      @app.route('/search_port', methods=['POST'])
      def search_port():
            portSearch = request.form['portSearch']
            return views.search_port_subDomain(portSearch)

      @app.route('/demo', methods=['POST'])
      def demo():
            return views.demo_site_nginx()
