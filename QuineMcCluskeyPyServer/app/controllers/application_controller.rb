class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  #protect_from_forgery with: :exception
protected
  def render_500
    respond_to do |format|
      format.html { render :file => "#{Rails.root}/public/500", :layout => false, :status => 500 }
      #format.xml  { head :not_found }
      #format.any  { head :not_found }
    end
  end
end
