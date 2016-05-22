from flask import render_template
from phase3 import app

#server/findings
@app.route("/findings")
def findings():
    with open('templates/findings.html', 'w') as html: #enter the output filename
	    html.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
 <link rel="stylesheet" type="text/css" href="templates/css/findings.css">
    <title>
      Chart
    </title>
    <link rel="stylesheet" href="templates/stylesheets/findings.css" type="text/css">
  </head>
<h1>Leeds</h1>
<p>Leeds, a city in West Yorkshire, England, was one of the leading centers of industry in Victorian England. (TripAdvisor)
They have realtime travel and traffic information for Leeds including live CCTV and mobile phone SMS services, live road traffic news and travel information, brought to you by BBC Travel and LeedsTravel.info</p>
  <script src="http://maps.google.com/maps/api/js?sensor=false"
          type="text/javascript"></script>
  <div id="map" style="min-width: 400px; height: 400px; margin: 0 auto"></div>

  <script type="text/javascript">
    var locations = [
      ['Leeds', 53.801277, -1.548567],
    ];

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: new google.maps.LatLng(53.801277, -1.548567),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
  </script>
<h1>Road Accidents</h1>
<h2>Observation 1</h2>
<p>In 2012, Males in Leeds are more likely to be in a car accident and be the casualty in comparision to Females.
The age group more likely to be in a car accident and be the casualty is from 15-35</p>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script src="http://code.jquery.com/jquery-1.9.1.js" type="text/javascript"></script>
<script src="http://code.highcharts.com/highcharts.js" type="text/javascript"></script>
<script src="http://code.highcharts.com/modules/exporting.js" type="text/javascript"></script>
<div id="container_a" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
<script type="text/javascript">
          $(function () {
              $('#container_a').highcharts({
                  chart: {
                      type: 'column'
                  },
                  title: {
                      text: 'Age of Casualty in Accidents Leeds 2012'
                  },
                  subtitle: {
                      text: 'Source: Leeds.com'
                  },
                  xAxis: {
                      categories: [
                            '0 -4',
                            '5 -9',
                            '10 -14',
                            '15 -19',
                            '20 -24',
                            '25 -29',
                            '30 -34',
                            '35 -39',
                            '40 -44',
                            '45 -49',
                            '50 -54',
                            '55 -59',
                            '60 -64',
                            '65 -69',
                            '70 -74',
                            '75 -79',
                            '80 -84',
                            '85 -89',
                            '90 -94',
                            '95 -99',
                      ],
                      crosshair: true
                  },
                  yAxis: {
                      min: 0,
                      title: {
                          text: 'Number of Casualties'
                      }
                  },
                  tooltip: {
                      headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                      pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                          '<td style="padding:0"><b>{point.y:4f}</b></td></tr>',
                      footerFormat: '</table>',
                      shared: true,
                      useHTML: true
                  },
                  plotOptions: {
                      column: {
                          pointPadding: 0.2,
                          borderWidth: 0
                      }
                  },
                  series: [{
                      name: 'Male',
                      data: [36,69,163,326,247,242,185,161,182,72,124,96,74,73,36,37,22,23,4,1]

                  }, {
                      name: 'Female',
                      data: [36,112,266,442,422,372,293,295,235,76,183,115,76,44,27,39,26,13,6,1]

                  }]
              });
          });
    </script>	
		''')
  
	    html.write('''
<h2>Observation 2</h2>
<p>Majority of vehicle accidents occur in a car. Other vehicles that are likely to be in a accident are bicycles, bus, or motorcyles. <p>  
<div id="container_b" style="min-width: 310px; height: 400px; max-width: 600px; margin: 0 auto"></div>
<script type="text/javascript">
$(function () {
    $('#container_b').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Type of Vehicle in Accidents Leeds 2012'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Vehicle',
            colorByPoint: true,
            data: [{
                name: 'Agricultural vehicle ',
                y: 2
            }, {
                name: 'Bus or Coach or Minibus',
                y: 193,
            }, {
                name: 'Car',
                y: 1882
            }, {
                name: 'Goods Vehicle',
                y: 84
            }, {
                name: 'Motorcycle',
                y: 190
            }, {
                name: 'Other',
                y: 18
            }, {
                name: 'Pedal Cycle',
                y: 262
            }, {
                name: 'Ridden Horse',
                y: 2
            }, {
                name: 'Taxi',
                y: 115           
            }]
        }]
    });
});
</script>
            ''')
            
	    html.write('''
<h2>Observation 3</h2>
<p>While poor weather conditions, lighting conditions, road surface is assumed to be cause vehicle accidents, this is not true. As seen in the graphs below fine weather,daylight and dry roads are the largest contributors to vehicle accidents.
And a reasonable assumption is that fine weather, daylight and dry roads is not the reason for vehicle accidents. <p>
<p1></p1>
<div id="container_c" style="float: left; width:33.33%; height: 400px; max-width: 600px; margin: 0 auto"></div><script type="text/javascript">
$(function () {
    $('#container_c').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Weather Conditions in Accidents Leeds 2012'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Vehicle',
            colorByPoint: true,
            data: [{
                name: 'Fine',
                y: 2450
            }, {
                name: 'Raining',
                y: 283                
            }, {
                name: 'Fog or Mist',
                y: 4,
            }, {
                name: 'Other',
                y: 5
            }, {
                name: 'Snowing',
                y: 4
         
            }]
        }]
    });
});
</script>
<div id="container_d" style="float: left; width: 33.33%; height: 400px; max-width: 600px; margin: 0 auto"></div>
<script type="text/javascript">
$(function () {

    $(document).ready(function () {

        // Build the chart
        $('#container_d').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                text: 'Lighting Conditions in Accidents Leeds 2012'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                name: 'Lighting Conditions',
                colorByPoint: true,
                data: [{
                    name: 'Darkness: street lights present but unlit',
                    y: 9
                }, {
                    name: 'Darkness: no street lighting',
                    y: 39,
                    sliced: true,
                    selected: true
                }, {
                    name: 'Darkness: street lighting unknown',
                    y: 670
                }, {
                    name: 'Darkness: street lights present and lit',
                    y: 472
                }, {
                    name: 'Daylight: street lights present',
                    y: 1558
                }]
            }]
        });
    });
});
</script>
<div id="container_e" style="float: left; width:33.33%; height: 400px; max-width: 600px; margin: 0 auto"></div>
<script type="text/javascript">
$(function () {
    $('#container_e').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Road Conditions in Accidents Leeds 2012'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Vehicle',
            colorByPoint: true,
            data: [{
                name: 'Flood',
                y: 5
            }, {
                name: 'Snow',
                y: 7                
            }, {
                name: 'Frost or Ice',
                y: 22,
            }, {
                name: 'Wet or Damp',
                y: 605
            }, {
                name: 'Dry',
                y: 2109
         
            }]
        }]
    });
});
</script>
<h3></h3>
<p>Instead, the data depicts that there is correlation with time period and vehicle accidents. As there are more car accidents during the time period 8am-8pm.
The assumption is that when there is a greater number of cars on the roads it causes vehicle accidents.</p>
<div id="container_f" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
<script type="text/javascript">
          $(function () {
              $('#container_f').highcharts({
                  chart: {
                      type: 'column'
                  },
                  title: {
                      text: 'Time periods of Accidents in Leeds 2012'
                  },
                  subtitle: {
                      text: 'Source: Leeds.com'
                  },
                  xAxis: {
                      categories: [
                            '0:00 -3:59',
                            '4:00 -7:59',
                            '8:00 -11:59',
                            '12:00 -15:59',
                            '16:00 -19:59',
                            '20:00 -23:59',
                      ],
                      crosshair: true
                  },
                  yAxis: {
                      min: 0,
                      title: {
                          text: 'Number of Accidents'
                      }
                  },
                  tooltip: {
                      headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                      pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                          '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                      footerFormat: '</table>',
                      shared: true,
                      useHTML: true
                  },
                  plotOptions: {
                      column: {
                          pointPadding: 0.2,
                          borderWidth: 0
                      }
                  },
                  series: [{
                      name: 'Time Periods',
                      data: [149,196,582,735,764,322]
                  }]
              });
          });
    </script>
            ''') 
            
            html.write('''
<h2>Observation 4</h2>
<p>In addition, month is not correleated with vehicle accidents, meaning every month has a similar chance of having a vehicle accident <p> 
<div id="container_g" style="min-width: 310px; height: 400px; max-width: 600px; margin: 0 auto"></div>
<script type="text/javascript">
$(function () {

    $(document).ready(function () {

        // Build the chart
        $('#container_g').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                text: 'Months in Accidents Leeds 2012'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                name: 'Lighting Conditions',
                colorByPoint: true,
                data: [{
                    name: 'January',
                    y: 186
                }, {
                    name: 'February',
                    y: 248,

                }, {
                    name: 'March',
                    y: 228
                }, {
                    name: 'April',
                    y: 189
                }, {
                    name: 'May',
                    y: 258
                }, {
                    name: 'June',
                    y: 192
                }, {
                    name: 'July',
                    y: 244
                }, {
                    name: 'August',
                    y: 259
                }, {
                    name: 'September',
                    y: 251
                }, {
                    name: 'October',
                    y: 249
                }, {
                    name: 'November',
                    y: 222
                }, {
                    name: 'December',
                    y: 222                   
                }]
            }]
        });
    });
});
</script>
            ''')
	    html.write('''
<h2>Observation 5</h2>
<p>Most vehicle accidents result in a severity of slight and driver and passenger are the casualties. <p> 
<div id="container_h" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
<script type="text/javascript">
          $(function () {
              $('#container_h').highcharts({
                  chart: {
                      type: 'column'
                  },
                  title: {
                      text: 'Casualty Class in Accidents Leeds 2012'
                  },
                  subtitle: {
                      text: 'Source: Leeds.com'
                  },
                  xAxis: {
                      categories: [
                            'Slight',
                            'Serious',
                            'Fatal',
                      ],
                      crosshair: true
                  },
                  yAxis: {
                      min: 0,
                      title: {
                          text: 'Number of Casualties'
                      }
                  },
                  tooltip: {
                      headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                      pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                          '<td style="padding:0"><b>{point.y:4f}</b></td></tr>',
                      footerFormat: '</table>',
                      shared: true,
                      useHTML: true
                  },
                  plotOptions: {
                      column: {
                          pointPadding: 0.2,
                          borderWidth: 0
                      }
                  },
                  series: [{
                      name: 'Driver',
                      data: [2534,180,11]

                  }, {
                      name: 'Passenger',
                      data: [2021,109,8]
                  }, {
                      name: 'Pedestrian',
                      data: [327,131,7]
                  }]
              });
          });
    </script>
<p>However, when passengers are the causalty there is a higher chance that it will be a serious accident.</p>
<div id="container_i" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
<script type="text/javascript">
          $(function () {
              $('#container_i').highcharts({
                  chart: {
                      type: 'column'
                  },
                  title: {
                      text: 'Casualty Class in Accidents Leeds 2012'
                  },
                  subtitle: {
                      text: 'Source: Leeds.com'
                  },
                  xAxis: {
                      categories: [
                            'Driver',
                            'Passeger',
                            'Pedestrian',
                      ],
                      crosshair: true
                  },
                  yAxis: {
                      min: 0,
                      title: {
                          text: 'Number of Casualties'
                      }
                  },
                  tooltip: {
                      headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                      pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                          '<td style="padding:0"><b>{point.y:4f}</b></td></tr>',
                      footerFormat: '</table>',
                      shared: true,
                      useHTML: true
                  },
                  plotOptions: {
                      column: {
                          pointPadding: 0.2,
                          borderWidth: 0
                      }
                  },
                  series: [{
                      name: 'Slight',
                      data: [2534,2021,327]

                  }, {
                      name: 'Serious',
                      data: [180,109,131]
                  }, {
                      name: 'Fatal',
                      data: [11,8,7]
                  }]
              });
          });
    </script>
<br>
<div id="container_j" style="min-width: 400px; height: 400px; margin: 0 auto"></div>
<script type="text/javascript">
          $(function () {
              $('#container_j').highcharts({
                  chart: {
                      type: 'column'
                  },
                  title: {
                      text: 'Casualty Class in Accidents Leeds 2012'
                  },
                  subtitle: {
                      text: 'Source: Leeds.com'
                  },
                  xAxis: {
                      categories: [
                            'Driver',
                            'Passeger',
                            'Pedestrian',
                      ],
                      crosshair: true
                  },
                  yAxis: {
                      min: 0,
                      title: {
                          text: 'Number of Casualties'
                      }
                  },
                  tooltip: {
                      headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                      pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                          '<td style="padding:0"><b>{point.y:4f}</b></td></tr>',
                      footerFormat: '</table>',
                      shared: true,
                      useHTML: true
                  },
                  plotOptions: {
                      column: {
                          pointPadding: 0.2,
                          borderWidth: 0
                      }
                  },
                  series: [{
                      name: 'Serious',
                      data: [180,109,131]
                  }, {
                      name: 'Fatal',
                      data: [11,8,7]
                  }]
              });
          });
    </script>
		''')
	    html.write('''
<h2>Conclusion</h2>
<p id=conclusion>Therefore, the overall contention is that there is a higher chance of a car accident if you are:
<br>
<br>
Using a vehicle during the peak periods- day time
<br>
Male aged between 15-35
<br>
If you are a driver or passenger
<br>
Or if you are in car , bicycle, bus, taxi or motorcyle
<br>
<br>
even if the weather conditions, month, road conditions or lighting conditions is poor.
</p>
''')
    return render_template("findings.html")
