#!/usr/bin/env python3
"""
위성 모니터링 데이터 분석 실행 스크립트
"""

import sys
import os
import argparse
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def main():
    parser = argparse.ArgumentParser(description='위성 모니터링 데이터 분석')
    parser.add_argument('--data-file', '-d', 
                       default='data/logs/system_logs/satellite_status.csv',
                       help='분석할 데이터 파일 경로')
    parser.add_argument('--output-dir', '-o',
                       default='data/analysis',
                       help='분석 결과 출력 디렉토리')
    parser.add_argument('--visualize', '-v', action='store_true',
                       help='시각화 결과 생성')
    
    args = parser.parse_args()
    
    # 출력 디렉토리 생성
    os.makedirs(args.output_dir, exist_ok=True)
    
    print("🔍 위성 모니터링 데이터 분석 시작...")
    
    try:
        # 데이터 분석기 임포트 및 실행
        from python.data_analyzer import SatelliteDataAnalyzer
        
        analyzer = SatelliteDataAnalyzer(args.data_file)
        
        # 기본 분석 실행
        print("📊 기본 통계 분석 중...")
        analyzer.analyze_basic_statistics()
        
        print("⚡ 전력 시스템 분석 중...")
        analyzer.analyze_power_trends()
        
        print("🌡️ 열관리 시스템 분석 중...")
        analyzer.analyze_thermal_behavior()
        
        print("🎯 자세제어 시스템 분석 중...")
        analyzer.analyze_attitude_control()
        
        print("📡 통신 시스템 분석 중...")
        analyzer.analyze_communication_performance()
        
        if args.visualize:
            print("📈 시각화 생성 중...")
            from python.visualization import SatelliteVisualizer
            visualizer = SatelliteVisualizer()
            visualizer.generate_dashboard(analyzer.get_data())
        
        print("✅ 분석 완료!")
        print(f"📁 결과 저장 위치: {args.output_dir}")
        
    except ImportError as e:
        print(f"❌ 모듈 임포트 오류: {e}")
        print("💡 Python 가상환경이 활성화되어 있는지 확인하세요.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ 데이터 파일을 찾을 수 없습니다: {args.data_file}")
        print("💡 먼저 모니터링 시스템을 실행하여 데이터를 생성하세요.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 분석 중 오류 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 