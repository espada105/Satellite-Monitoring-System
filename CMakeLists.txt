cmake_minimum_required(VERSION 3.16)
project(SatelliteMonitoringSystem VERSION 1.0.0 LANGUAGES CXX)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 컴파일러 플래그
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")
endif()

# 소스 파일들
set(SOURCES
    src/main.cpp
    src/core/satellite_monitor.cpp
    src/subsystems/power_system/power_system.cpp
    src/subsystems/thermal_system/thermal_system.cpp
    src/subsystems/attitude_system/attitude_system.cpp
    src/subsystems/communication_system/communication_system.cpp
    src/monitoring/data_logger.cpp
    src/monitoring/alert_system.cpp
    src/monitoring/status_reporter.cpp
    src/utils/math_utils.cpp
    src/utils/time_utils.cpp
    src/utils/config_parser.cpp
)

# 헤더 파일들
set(HEADERS
    src/core/satellite_monitor.h
    src/core/system_status.h
    src/core/constants.h
    src/subsystems/power_system/power_system.h
    src/subsystems/power_system/power_status.h
    src/subsystems/thermal_system/thermal_system.h
    src/subsystems/thermal_system/thermal_status.h
    src/subsystems/attitude_system/attitude_system.h
    src/subsystems/attitude_system/attitude_status.h
    src/subsystems/communication_system/communication_system.h
    src/subsystems/communication_system/communication_status.h
    src/monitoring/data_logger.h
    src/monitoring/alert_system.h
    src/monitoring/status_reporter.h
    src/utils/math_utils.h
    src/utils/time_utils.h
    src/utils/config_parser.h
    src/models/vector3d.h
    src/models/quaternion.h
    src/models/system_log.h
)

# 실행 파일 생성
add_executable(satellite_monitor ${SOURCES} ${HEADERS})

# 헤더 파일 경로 설정
target_include_directories(satellite_monitor PRIVATE src)

# 테스트 설정 (Google Test 사용)
enable_testing()
find_package(GTest QUIET)
if(GTest_FOUND)
    add_subdirectory(tests)
endif()

# 설치 설정
install(TARGETS satellite_monitor DESTINATION bin) 