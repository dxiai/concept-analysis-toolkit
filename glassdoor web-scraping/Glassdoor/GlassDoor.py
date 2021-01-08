#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 10:28:28 2019

@author: bodr
"""

import urllib.request
import re
import json

class JobAd:
    def __init__(self, title, company, industry, description):
        self.title = title
        self.company = company
        self.industry = industry
        self.description = description
        
def convert_to_dict(obj):
  """
  A function takes in a custom object and returns a dictionary representation of the object.
  """
 
  obj_dict = {}
  
  #  Populate the dictionary with object properties
  obj_dict.update(obj.__dict__)
  
  return obj_dict


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
baseurl = 'https://de.glassdoor.ch/Job/zuerich-life-science-data-jobs-SRCH_IL.0,6_IC3297851_KE7,24_IP2.htm?radius=124&industryId=1020'
baseurl = 'https://de.glassdoor.ch/Job/jobs.htm?sc.keyword=Data%20Life%20Science&locT=C&locId=3297851&locKeyword=Zuerich&jobType=all&fromAge=-1&radius=124&cityId=-1&minRating=0.0&industryId=1020&sgocId=-1&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
prepageurl = 'https://de.glassdoor.ch/Job/zuerich-life-science-data-jobs-SRCH_IL.0,6_IP2.htm'
prepageurl = 'https://de.glassdoor.ch/Job/zuerich-life-science-data-jobs-SRCH_IL.0,6_IC3297851_KE7,24.htm?radius=124&industryId=1020?jobListing.htm='
postpageurl = ''
adurl = 'https://de.glassdoor.ch/partner/jobListing.htm?pos=201&ao=567668&s=58&guid=0000016e22b67b139ec4036f99dd2126&src=GD_JOB_AD&t=SR&extid=1&exst=EL&ist=&ast=EL&vt=w&slr=true&cs=1_ec734d42&cb=1572540414983&jobListingId='
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Referer': 'https://cssspritegenerator.com',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}

request = urllib.request.Request( baseurl, None, hdr )
page = urllib.request.urlopen( request )
html = page.read().decode( 'utf-8-sig' )
pages = int(re.findall( 'Seite 1 von ([0-9]+)', html )[0])

jobAds = []

print( "Fetching job offers..." )
print( "Found", pages, "pages" )

for i in range(1,pages):
    print( "Processing page", i )

    pageurl = prepageurl + str(i) + postpageurl
    request = urllib.request.Request( pageurl, None, hdr )
    page = urllib.request.urlopen( request )
    html = page.read().decode( 'utf-8-sig' )
    jobids = re.findall( "\'([0-9]{10}?)\'", html )
    print( "Found", len(set(jobids)), "offers" )
    
    for jobid in set(jobids):
        print( "Processing offer", adurl + jobid )
        
        request = urllib.request.Request( adurl + jobid, None, hdr )
        page = urllib.request.urlopen( request )
        html = page.read().decode( 'utf-8-sig' )
        title = re.findall( 'jobTitle..: "([\s\S]*?)"', html )
        industry = re.findall( '.industry.: "([\s\S]*?)"', html )
        company = re.findall( '.name.: "([\s\S]*?)"', html )
        print( "Job: ", title, "Industry: ", industry, "Company:", company )

        offer = re.findall( '.description.: "([\s\S]*?)\/script', html )
        jobAds.append( JobAd( str(title)[2:-2], str(company)[2:-2], str(industry)[2:-2], str(offer)[2:-2] ))


jsonJobs = json.dumps( jobAds, default = convert_to_dict )
    
FILE = open( './Jobs.json', "w" )
FILE.write( jsonJobs )
FILE.close()



