class QuineController < ApplicationController
	def index
		minterms = params[:minterms]
		dontcares = params[:dontcares]
		variables = params[:Variables]
		cmd = "python quine_working.py '{\"minterms\":\"#{minterms}\",\"dontcares\":\"#{dontcares}\",\"Variables\":\"#{variables}\"}'"
		execCmd =  `#{cmd}`
		render inline: execCmd
	end
end
